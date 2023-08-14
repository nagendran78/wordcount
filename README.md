# wordcount
Python code to calculate and provide a summary of words counts 

## Requirements
* The following items are required to run wordcount. Please download [Python 3.8.2](https://www.python.org/downloads/) or later version
* To verify open cli and run
  * python3 --version

## Running the Application
1. Download and install Python3.x.x interpreter.  
2. Git clone this repository.
3. Configure the **`wordcount.cfg`** appropriately if the data samples need to be updated
4. If new data sample is to be used for testing `without` changing the code.
   * Access the directory **[\datasamsple]**
   * Rename the file from **`sample01.txt`** to **`sample01_old.txt`** 
   * Create new file **`sample01.txt`**
   * Goto cli and run
     * python3 wordcount.py
5. If new data sample is to be used and `preserving all the existing sample files`.
   * Upload the new sample file for example **`sample04.txt`** at directory **[\datasample]**
   * Edit the configuration file **`wordcount.cfg`**
   * Add the followng entry in the configuration file 
     * **`filename04 = sample04.txt`**
   * Modify the python code file **`wordcount.py`**
     * Search for variable assignment `file_name`
     * Update the config value to the sample file which is **`filename_04`**
   * Save the **`wordcount.py`** and **`wordcount.cfg`**
   * goto cli and run
     * python wordcount.py


## Configuration [wordcount.cfg]
**Configuration File Details**

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
|data_directory|Location of datafile|string|datasample|yes|
|filename_01|Sample file with simple words|string|sample01.txt|yes|
|filename_02|Sample file with longer words and with multiple lines|string|sample02.txt|no|
|filename_03|Same sample file as "sample01.txt" but words are reversed|string|sample03.txt|no|
