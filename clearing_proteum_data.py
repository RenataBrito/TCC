import sys
import os


def main():
    if len(sys.argv) < 6:
        print("error: clearing_proteum_data.py <base_dir> <prog> <firstMutant> <lastMutant> <stringPattern>")
        print("Example ubuntu: ?")
        print("Example ubuntu in windows: python3 clearing_proteum_data.py /mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum sum 0 2 funlockfile")
        sys.exit(1)

    baseDir = sys.argv[1]
    outputDir = baseDir + "/" + "mutants"
    prog = sys.argv[2]
    firstMutant = int(sys.argv[3])
    lastMutant = int(sys.argv[4])
    stringPattern = sys.argv[5]

    # Creating outputDir if it not exist
    isExist = os.path.exists(outputDir)
    if (not isExist):
        cmd = "mkdir " + outputDir
        os.system(cmd)

    print("\nRemoving pre-processing code from mutant")
    for MUT in range(firstMutant, lastMutant+1):
        cmd = "cd " + baseDir + ";awk \'{if($3==\""+stringPattern+"\"){flag=1;next} else if (flag){print $0}}\' muta"+str(
            MUT)+"_"+prog+".c > " + outputDir + "/muta"+str(MUT)+"_" + prog+".c; rm muta" +str(MUT)+"_" + prog+".c"
        print(".", end="")
        os.system(cmd)


if __name__ == "__main__":
    main()
