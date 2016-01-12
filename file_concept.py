#now starting how to write to a file through the py

text="this is the first python file being created\n";

saveFile = open("example.txt","w");
saveFile.write(text);
saveFile.close();
