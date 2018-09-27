import copy
import time
import numpy as np

from printrun.printcore import printcore


class Positioner(object):
    def __init__(self, device_file, zero_pos, feed_rate, bounds=None, home=True, wait=True):
        self.printer = printcore(device_file, 115200)
        time.sleep(0.2)
        self.zero_pos = self._assert_pos(zero_pos)
        self.feed_rate = feed_rate
        self.wait = wait

        if bounds is None:
            # Define some sane bounds
            self.bounds = np.array([40, 40, 210])
        else:
            self._assert_pos(bounds)
            self.bounds = bounds

        # Printcore is one of the worst python libraries I've ever seen.
        # It's basically impossible to read anything back from the printer without tonnes of work.
        self.current_pos = None
        if home:
            self.home()

    @staticmethod
    def _assert_pos(pos):
        assert len(pos) == 3
        return pos

    def home(self):
        self.printer.send('G28')
        self.current_pos = None
        if self.wait:
            time.sleep(4)

    def _calculate_transit_time(self, pos):
        feed_rate_mm_per_s = self.feed_rate / 60
        if self.current_pos is None:
            # Since we don't know where we are, assume that we have to move from at least 250mm in the Z axis
            current_pos = np.array([0,0,250])
        else:
            current_pos = self.current_pos

        # As should be expected, the printer does not actually move at a constant rate throughout its volume
        # The Z rate seems to be half of what it should be
        xy_transit_time = np.linalg.norm(current_pos[:2] - pos[:2]) / (feed_rate_mm_per_s)
        z_transit_time = np.abs(current_pos[2] - pos[2]) / ((feed_rate_mm_per_s/2.0) * 1.2)
        total_transit_time = xy_transit_time + z_transit_time
        return max(xy_transit_time, z_transit_time) + total_transit_time / 10

    def _goto_raw(self, pos):
        self._assert_pos(pos)
        self._check_bounds(pos)
        self.printer.send("G1 X{0:.2f} Y{1:.2f} Z{2:.2f} F{3}".format(pos[0], pos[1], pos[2], self.feed_rate))
        if self.wait:
            time.sleep(self._calculate_transit_time(pos))
        self.current_pos = pos

    def _check_bounds(self, pos):
        if not all(np.abs(pos) <= self.bounds):
            raise ValueError(
                "Cannot move to position {p[0]},{p[1]},{p[2]} as it lies outside the bounds {b[0]},{b[1]},{b[2]}"
                    .format(p=pos, b=self.bounds)
            )
        if pos[2] < self.zero_pos[2]:
            raise ValueError(
                "Cannot move to position {p[0]},{p[1]},{p[2]} as the Z value lies below the zero Z of {z[2]}"
                    .format(p=pos, z=self.zero_pos)
            )

    def goto(self, pos):
        """Go to a position relative to the zero position"""
        self._assert_pos(pos)
        self._goto_raw(pos + self.zero_pos)

    def zero(self):
        self.goto(np.array([0, 0, 0]))

    def close(self):
        self.printer.disconnect()


class PositionSweeperStep(object):
    def __init__(self, position):
        self.position = copy.copy(position)

    def __repr__(self):
        return "{0}".format(self.position)


class PositionSweeper(object):
    def __init__(self, positioner, start_pos, stop_pos, step_count):
        self.positioner = positioner
        self.start_pos = start_pos
        self.stop_pos = stop_pos
        self.step_count = step_count

    def __call__(self, *args, **kwargs):
        if self.step_count < 2:
            self.positioner.goto(self.start_pos)
            yield PositionSweeperStep(self.start_pos)
            return

        step_vector = (self.stop_pos - self.start_pos) / (self.step_count - 1)

        step_pos = self.start_pos
        for step in xrange(self.step_count):
            self.positioner.goto(step_pos)
            yield PositionSweeperStep(step_pos)
            step_pos += step_vector


class NDimensionalPositionSweeper():
    def __init__(self, positioner, start_pos, stop_pos, step_size):
        self.positioner = positioner
        self.start_pos = start_pos
        self.stop_pos = stop_pos
        self.step_size = step_size

    def __call__(self, *args, **kwargs):
        x_min = int(min(self.start_pos[0], self.stop_pos[0]))
        y_min = int(min(self.start_pos[1], self.stop_pos[1]))
        z_min = int(min(self.start_pos[2], self.stop_pos[2]))

        x_max = int(max(self.start_pos[0], self.stop_pos[0])) + self.step_size
        y_max = int(max(self.start_pos[1], self.stop_pos[1])) + self.step_size
        z_max = int(min(self.start_pos[2], self.stop_pos[2])) + self.step_size

        for z in range(z_min, z_max, self.step_size):
            for y in range(y_min, y_max, self.step_size):
                for x in range(x_min, x_max, self.step_size):
                    step_pos = np.array([x, y, z])
                    self.positioner.goto(step_pos)
                    yield PositionSweeperStep(step_pos)
