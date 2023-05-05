import sys
import os


def main():
    if len(sys.argv) < 5:
        print("error: clearing_proteum_data.py <base_dir> <prog> <path_to_mutant_numbers_file> <stringPattern>")
        print("Example: python3 clearing_proteum_data.py /mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum sum /mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/sum/equivalents_sum.txt funlockfile")
        print("Example: python3 clearing_proteum_data.py /mnt/c/Users/renat/Desktop/TCC/projeto/TCC/programs/tcas tcas 0 2 getloadavg")
        sys.exit(1)
    

    baseDir = sys.argv[1]
    prog = sys.argv[2]
    stringPattern = sys.argv[-1]

    if len(sys.argv) == 6:
        firstMutant = int(sys.argv[3])
        lastMutant = int(sys.argv[4])
        path_to_mutants = None
    else:
        path_to_mutants = sys.argv[3]
        firstMutant = None
        lastMutant = None
        with open(path_to_mutants, "r") as file:
            contents = file.read()
            mutants = [int(mutant) for mutant in contents.split()]

    outputDir = baseDir + "/" + "mutants"

    # Creating outputDir if it not exist
    isExist = os.path.exists(outputDir)
    if (not isExist):
        cmd = "mkdir " + outputDir
        os.system(cmd)

    if path_to_mutants is None:
        for MUT in range(firstMutant, lastMutant+1):
            print("\nRemoving pre-processing code from mutant: ", MUT)
            cmd = "cd " + baseDir + ";awk \'{if($3==\""+stringPattern+"\"){flag=1;next} else if (flag){print $0}}\' muta"+str(
                MUT)+"_"+prog+".c > " + outputDir + "/muta"+str(MUT)+"_" + prog+".c; rm muta" +str(MUT)+"_" + prog+".c"
            os.system(cmd)
    else:
        for MUT in mutants:
            print("\nRemoving pre-processing code from mutant: ", MUT)
            cmd = "cd " + baseDir + ";awk \'{if($3==\""+stringPattern+"\"){flag=1;next} else if (flag){print $0}}\' muta"+str(
                MUT)+"_"+prog+".c > " + outputDir + "/muta"+str(MUT)+"_" + prog+".c; rm muta" +str(MUT)+"_" + prog+".c"
            os.system(cmd)


if __name__ == "__main__":
    main()
