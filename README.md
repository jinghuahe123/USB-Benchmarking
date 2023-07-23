# USB-Benchmarking
Used to constantly write to a user-specified directory as a form of stress-testing.

On launch, you should be greeted with an input for the "Source", and after you enter a directory, an input for "Destination". These should both be directories that look something like this: "C:\test\testfolder". The program will create a log file called debug.log to record each cycle's end time. As said, please do not use any directories that have important files in them in the case that the program glitches out and corrupts them. I will also not be responsible for drives that die under the torture of being constantly written to and read from. Use at your own risk.

# How to use the program:
On launch, you should be greeted with a paragraph of text which contain warnings. Please read thoroughly. Below you should see a line that says "Source (Must Exist):". Enter an existing source directory that contains certain files that you would like to be used in the program as stress files (i.e. they will be written to the target directory over and over". The next input looks like "Destination (Must NOT Exist):" and requires you to enter a non-existing directory which the program will create and where the program will write the files in the directory specified in the first step. The program will then begin the process of copy and deleting, and depending on how large your test files are and how fast your target disk is, the program will slowly or quite rapidly ouptut the end time of each cycle. This will be mirrored in the log file that is created. 

Known issues: 
* If program crashes before completing the first cycle, you will need to manually go inside the debug.log file and delete the last line that begins with a time and ends with "Program Started" or "Program Restarted". Make sure there is only one empty line at the end of the log file after the last cycle is recorded.
* The program does not know how to handle a directory that does not exist if specified needs to exist or a directory that exists when specified must not exist. In this case the program will crash and you will need to manually delete or create the directories as specified. 
