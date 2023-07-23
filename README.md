# USB-Benchmarking
Used to constantly write to a user-specified directory as a form of stress-testing.

On launch, you should be greeted with an input for the "Source", and after you enter a directory, an input for "Destination". These should both be directories that look something like this: "C:\test\testfolder". The program will create a log file called debug.log to record each cycle's end time. As said, please do not use any directories that have important files in them in the case that the program glitches out and corrupts them. I will also not be responsible for drives that die under the torture of being constantly written to and read from. Use at your own risk.

Known issues: 
* If program crashes before completing the first cycle, you will need to manually go inside the debug.log file and delete the last line that begins with a time and ends with "Program Started" or "Program Restarted". Make sure there is only one empty line at the end of the log file after the last cycle is recorded.
* The program does not know how to handle a directory that does not exist if specified needs to exist or a directory that exists when specified must not exist. In this case the program will crash and you will need to manually delete or create the directories as specified. 
