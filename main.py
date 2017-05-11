import browserArtifacts
import jumpLists
import lastVistiedMRU
import openSaveMRU
import runMRU
import shimCache
import string



def output_report(report):
    choice = ""
    while choice != 'q':
        print("""Please select how to output report:
[P]rint to terminal.
[O]utput to file.
[B]ack.""")
        choice = input("[Q]uit.").lower()
        if choice=='p':
            print(report)
        elif choice == 'o':
            filename = input("Please specify the file name you would like to output the report:")
            with open(filename, 'w+') as f:
                for line in report:
                    f.write(line)
        elif choice == 'b':
            return
        elif choice=='q':
            exit()
        else:
            print("Invalid Input.")
def forensics():
    if __name__=='__main__':
        report = ""

        userChoice = ""
        while(userChoice!='q'):
            print("""Please select from the following options:
[A]pplication Compatability Cache.
[B]rowser Artifacts.
[J]ump Lists.
[L]ast Visited Most Recently Used.
[O]pen Save Dialog Most Recently Used.
[R]un Command History.
[F]ull Report.
[S]ettings.""")
            userChoice = input("[Q]uit.").lower()
            if userChoice == 'a':
                report += shimCache.pull_shim_cache()
                output_report(report)
            elif userChoice == 'b':
                report += browserArtifacts.pull_chrome_artifacts()
                output_report(report)
            elif userChoice == 'j':
                report += jumpLists.pull_jump_lists()
                output_report(report)
            elif userChoice == 'l':
                report += lastVistiedMRU.pull_last_visited_mru()
                output_report(report)
            elif userChoice == 'o':
                report += openSaveMRU.pull_open_save_mru()
                output_report(report)
            elif userChoice == 'r':
                runMRU.pull_run_mru()
                output_report(report)
            elif userChoice == 'f':
                report += shimCache.pull_shim_cache()
                report += browserArtifacts.pull_chrome_artifacts()
                report += jumpLists.pull_jump_lists()
                report += lastVistiedMRU.pull_last_visited_mru()
                report += openSaveMRU.pull_open_save_mru()
                report += runMRU.pull_run_mru()
                output_report(report)
            elif userChoice == 'q':
                exit(0)
            else:
                print("Incorrect Input.")
forensics()