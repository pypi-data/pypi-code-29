import glob
import os
import shutil


def convert(filepath: str) -> None:
    content = open(filepath).readlines()
    check_line = content[0]
    if not check_line.startswith("#"):
        print("Missing checkline: ", filepath)

    code = check_line.split("/")[-1]
    if not code.startswith("RSPEC-"):
        print("Wrong code line in: ", filepath)

    # with open(code.strip() + ".py", "w") as out:
    #     out.write("import bblfsh_sonar_checks.utils as utils\n\n")
    #     out.write("import bblfsh\n\n")
    #     firstidx = 0
    #
    #     for idx, line in enumerate(content[1:]):
    #         if "client.parse" in line:
    #             firstidx = idx + 2
    #             break
    #
    #     newcontent = content[firstidx:]
    #
    #     out.write("def check(uast):\n")
    #     out.write("    findings = []\n\n")
    #
    #     for line in newcontent:
    #         if "print(" in line:
    #             line = line.replace('print(', 'findings.append({"msg": ')
    #         out.write("    " + line)
    #
    #     out.write("\n    return findings\n\n")
    #
    #     out.write("if __name__ == '__main__': utils.run_default_fixture(__file__, check)\n")

    # shutil.copy("../../fixtures/java/%s.java" % filepath[:-3],
    #             "../../fixtures/java/%s.java" % code.strip())

    shutil.copy("../../../exported_uast/java/%s.java.native" % filepath[:-3],
                "../../../exported_uast/java/%s.java.native" % code.strip())

    shutil.copy("../../../exported_uast/java/%s.java.uast" % filepath[:-3],
                "../../../exported_uast/java/%s.java.uast" % code.strip())

    shutil.copy("../../../exported_uast/java/%s.java.sem.uast" % filepath[:-3],
                "../../../exported_uast/java/%s.java.sem.uast" % code.strip())
def main():
    files = glob.glob("*.py")

    for f in files:
        if f in ("convert.py", "__init__.py") or f.startswith("RSPEC-"):
            continue

        convert(f)


if __name__ == "__main__":
    main()
