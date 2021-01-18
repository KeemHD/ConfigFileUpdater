#place config txt file inside configFiles folder
#located in the same directory as the application
#updated files will be place in the updatedConfigFiles folder

#NOTE: each time the application is ran the
# data inside the updatedConfigFiles folders
# may be overwritten!

import pathlib

def open_file(folder_name):
    key_to_update = input("Key to change ")
    replacement_value = input("Replace with ")

    #loops through files located in the
    for path in pathlib.Path(folder_name).iterdir():
        print("Looking to update-> "+ str(path))
        current_file = open(path, 'r+')

        file_name = ""
        backslash_found = False

        # loop is used to build a copy of the
        # original files name
        for c in str(path):
            if backslash_found:
                file_name += str(c)

            elif c == "\\":
                backslash_found = True


        update_file(current_file,key_to_update,replacement_value,file_name)
        current_file.close()

    #used if more updates are needed
    continue_to_update = input("Enter 1 to continue to update; 0 to exit")
    if continue_to_update == "1":
        open_file("updatedConfigFiles")


#opens a file to store the updated config files
def update_file(file,key,replacement_value,file_name):

    name = "updatedConfigFiles\\"+file_name
    update_file = open(name,"r+")

    key_found = False
    #loops each line of file searching the key
    for line in file:
        if key in line or key_found:
            if len(replacement_value) > 0:
                #replaces "0" values in current line of the file
                # if there are replacement values available
                #replace_line return the remainder of replacement values
                # that would not fit on  current file line
                replacement_value = replace_line(update_file,line,replacement_value)
                key_found = True

            else:
                key_found = False
                update_file.write(line)
            print(name + " was updated!\n")

        else:
            update_file.write(line)


    update_file.close()


#replace_line() called by update_file()
#accepts file that will be updated
#accepts
#accepts a string of users replacement values
#
def replace_line(file,file_line,replacement_value):
    list_of_values = replacement_value.split(" ")

    #replace first occurrences of 0 on the file line
    while "0" in file_line and len(list_of_values)>0:
        file_line = file_line.replace('0', list_of_values[0], 1)
        list_of_values.pop(0)

    #this writes the updated file line to the new
    # file inside the updatedConfigFilesFolder
    file.write(file_line)


    #builds a string of the remaining values that needs
    # to be inserted into the updated files
    remaining_replacement_values = ""
    for v in list_of_values:
        remaining_replacement_values += v
        remaining_replacement_values +=" "


    #[:-1] used to not return last empty space character
    return remaining_replacement_values[:-1]

#main
if __name__ == '__main__':
    open_file("configFiles")
