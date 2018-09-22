# -*- coding: utf-8 -*-
import binascii
import hashlib
import logging
import os
import pickle
from pathlib import Path

import time


class CacheLite(object):
    log = logging.getLogger(__name__)

    def __init__(self, dir, raise_write_error=False, raise_read_error=False, lock_file_purge_sec=1):

        self._dir = Path(dir)
        self._hash_cost_func = hashlib.sha1
        self._raise_write_error = raise_write_error
        self._raise_read_error = raise_read_error
        self._lock_file_purge_sec = lock_file_purge_sec
        if not self._dir.exists():
            self._dir.mkdir()

    def __len__(self):
        files = self._dir.glob("*.pkl")
        key_cnt = 0
        for file_path in files:
            try:
                contents = self._read_and_verify_contents_from_file(file_path)
                key_cnt += len(contents)
            except BaseException:
                pass
        return key_cnt

    def __contains__(self, item):
        try:
            self.__getitem__(item)
            return True
        except KeyError:
            return False

    def __iter__(self):
        files = self._dir.glob("*.pkl")
        cache_it = CacheLiteIterator(files)
        return cache_it

    def clear(self):
        files = self._dir.glob("*.pkl")
        for file_path in files:
            file_path.unlink()

    def items(self):
        files = self._dir.glob("*.pkl")
        return CacheLiteIterator(files, ret_value=CacheLiteIterator.RET_KEY_VALUE)

    def keys(self):
        files = self._dir.glob("*.pkl")
        return CacheLiteIterator(files, ret_value=CacheLiteIterator.RET_KEY_ONLY)

    def values(self):
        files = self._dir.glob("*.pkl")
        return CacheLiteIterator(files, ret_value=CacheLiteIterator.RET_VALUE_ONLY)

    def __setitem__(self, key, value):

        file_name = self._key_to_file_path(key)
        target_file = self._dir / file_name.with_suffix(".pkl")
        lock_file = self._file_path_to_lock_file_path(target_file)
        next_file = self._file_path_to_next_file_path(target_file)
        if os.path.exists(target_file):
            if not os.path.exists(lock_file):
                # file exists, but not lockfile
                try:
                    with open(lock_file, "w") as f:
                        f.close()

                    obj_contents = self._read_contents_from_file(target_file)
                    target_pos = -1
                    for pos, data in enumerate(obj_contents):
                        cur_key, cur_value = data
                        if cur_key == key:
                            target_pos = pos
                    if target_pos > -1:
                        obj_contents[target_pos] = [key, value]
                    else:
                        obj_contents.append([key, value])
                    str_contents = pickle.dumps(obj_contents)
                    self._write_and_verify(target_file, next_file, lock_file, str_contents, key)
                    os.remove(lock_file)
                except BaseException as e:
                    if os.path.exists(lock_file):
                        os.remove(lock_file)
                    raise e
                return

            else:
                if self._raise_write_error:
                    raise CacheLiteWriteError("WriteError lockfile exists! key:%s file:%s" % (key, target_file))
                return

        else:
            if not os.path.exists(lock_file):
                try:
                    with open(lock_file, "w") as f:
                        f.close()
                    str_contents = self._to_new_value_str(key, value)
                    r = self._write_and_verify(target_file, next_file, lock_file, str_contents, key)
                    os.remove(lock_file)

                except BaseException as e:
                    if os.path.exists(lock_file):
                        os.remove(lock_file)
                return
            else:
                # os.path.getctime(lock_file)
                if self._raise_write_error:
                    raise CacheLiteWriteError("WriteError lockfile exists! key:%s file:%s" % (key, target_file))

                return

    def _write_and_verify(self, target_file, next_file, lock_file, str_contents, key):
        crc = self._to_signature(str_contents)
        with open(next_file, "wb") as f:
            f.write(pickle.dumps(
                [crc, str_contents]
            ))
        # rename
        try:
            os.rename(next_file, target_file)
        except IOError:
            self.log.warning("write error maybe interrupted by other process or thread")
            if os.path.exists(next_file):
                os.remove(next_file)

        with open(target_file, "rb") as target_strm:
            sig, bin_data = pickle.load(target_strm)
        r = self._verify_signature(bin_data, sig)
        if r:
            return True
        else:
            # if sinigure not match
            if os.path.exists(target_file):
                os.remove(target_file)
            if self._raise_write_error:
                raise CacheLiteWriteError(key)
            else:
                return False

    def __getitem__(self, key):
        file_path = self._key_to_file_path(key)
        try:
            contents = self._read_and_verify_contents_from_file(file_path)
            if contents:
                for k_v_pair in contents:
                    if k_v_pair[0] == key:
                        return k_v_pair[1]
                    raise KeyError(key)

            else:
                if self._raise_read_error:
                    raise CacheLiteReadError("KeyError:%s" % key)
        except FileNotFoundError:
            pass
        except BaseException:
            raise
        raise KeyError(key)

    def __delitem__(self, key):
        file_name = self._key_to_file_path(key)
        target_file = self._dir / file_name.with_suffix(".pkl")
        if os.path.exists(target_file):
            lock_file = self._file_path_to_lock_file_path(target_file)
            next_file = self._file_path_to_next_file_path(target_file)
            # print(target_file, lock_file, next_file)
            if not os.path.exists(lock_file):
                # file exists, but not lockfile
                try:
                    obj_contents = self._read_contents_from_file(target_file)
                    target_pos = -1
                    if len(obj_contents) is 0:
                        try:
                            os.remove(target_file)
                        except FileNotFoundError:
                            pass
                        return
                    else:
                        # seek the pos from list
                        for pos, data in enumerate(obj_contents):
                            cur_key, cur_value = data
                            if cur_key == key:
                                target_pos = pos
                        # delete or contents
                        if target_pos > -1:
                            del obj_contents[target_pos]
                            # delete file if there are no contents
                            if len(obj_contents) == 0:
                                os.remove(target_file)
                                return
                            else:
                                # update contents
                                with open(lock_file, "w") as f:
                                    f.close()
                                str_contents = pickle.dumps(obj_contents)
                                self._write_and_verify(target_file, next_file, lock_file, str_contents, key)
                                os.remove(lock_file)
                                return
                        else:
                            raise KeyError(key)
                except FileNotFoundError:
                    pass

                except BaseException as e:
                    self.log.error(e)

                raise KeyError(key)


            else:
                file_ts = os.path.getctime(lock_file)
                cur_ts = time.time()
                if cur_ts - file_ts > self._lock_file_purge_sec:
                    os.remove(lock_file)
                    return self.__delitem__(key)
                if self._raise_write_error:
                    raise CacheLiteWriteError(key)
        else:
            raise KeyError(key)

    @staticmethod
    def _read_and_verify_contents_from_file(target_file):
        with open(target_file, "rb") as f:
            sig, bin_data = pickle.load(f)
        r = CacheLite._verify_signature(bin_data, sig)
        if r:
            return pickle.loads(bin_data)
        else:
            return None

    @staticmethod
    def _read_contents_from_file(target_file):
        with open(target_file, "rb") as f:
            sig, bin_data = pickle.load(f)
        return pickle.loads(bin_data)

    def _key_to_file_path(self, key) -> Path:
        base_name = self._hash_cost_func(bytes(key, encoding='utf-8')).hexdigest()
        file_path = self._dir / (base_name + (".pkl"))
        return file_path

    @staticmethod
    def _file_path_to_lock_file_path(file_path) -> Path:
        return file_path.with_suffix(".lock")

    @staticmethod
    def _file_path_to_next_file_path(file_path) -> Path:
        return file_path.with_suffix(".next")

    @staticmethod
    def _to_signature(contents):
        return binascii.crc32(contents)

    @staticmethod
    def _verify_signature(contents, sig):
        return binascii.crc32(contents) == sig

    def _to_new_value_str(self, key, value):
        return pickle.dumps(
            [
                [key, value]
            ]
        )


class CacheLiteError(BaseException):
    pass


class CacheLiteWriteError(CacheLiteError):
    pass


class CacheLiteReadError(CacheLiteError, KeyError):
    pass


class CacheLiteIterator:
    RET_KEY_ONLY = 1
    RET_VALUE_ONLY = 2
    RET_KEY_VALUE = 3

    def __init__(self, file_list, ret_value=RET_KEY_ONLY):

        self._file_list = file_list
        self._ret_value_type = ret_value
        self._insdie_it = file_list
        self._cur_file_path = next(self._insdie_it)
        self._cur_file_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        while (True):
            try:
                with open(self._cur_file_path, "rb") as f:
                    sig, bin_data = pickle.load(f)
                r = CacheLite._verify_signature(bin_data, sig)
                if r:
                    contents = pickle.loads(bin_data)
                    for i, k_v_pair in enumerate(contents):
                        if i < self._cur_file_pos:
                            continue
                        self._cur_file_pos = i + 1

                        if self._ret_value_type is self.RET_KEY_VALUE:
                            return (k_v_pair[0], k_v_pair(1))
                        elif self._ret_value_type is self.RET_KEY_ONLY:
                            return k_v_pair[0]
                        else:
                            return k_v_pair[1]
                    self._cur_file_pos = 0

                self._cur_file_path = next(self._insdie_it)

            except StopIteration as e:
                break
            except FileNotFoundError as e:
                pass
            except BaseException as e:
                pass

        raise StopIteration
