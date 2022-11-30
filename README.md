# 4124-xmlperformance-testdata

This repository contains test data for measuring the performance of the xmlupload. 

## Description of the test data

The folder `bistreams` contains test files in the formats

 - docx
 - jpeg
 - mp3
 - mp4
 - txt
 - zip

For each of these formats, there is a file of the (approximate) size

 - 0.1 MB
 - 1 MB
 - 10 MB
 - 100 MB

There are different XML data files that follow different testing strategies:

 - `all_files.xml` contains every bitstream once (24 bitstreams --> 24 resources).
 - `no_files_x_links_x_textfields.xml` contains 1000 resources of type `Resource`, each having x resptr-links and x text fields (where 0 <= x < 5).
 - `one_file.xml` contains 1000 identical `StillImageRepresentation`s that all contain the same 1 MB JPEG image.


## Steps to do performance measures

First, create the project `xmlperformance` with 

```
dsp-tools create xmlperformance.json
```

Then, upload the data files with

```
dsp-tools xmlupload --metrics xml_files/all_files.xml
dsp-tools xmlupload --metrics xml_files/no_files_0_links_0_textfields.xml
dsp-tools xmlupload --metrics xml_files/no_files_1_links_1_textfields.xml
dsp-tools xmlupload --metrics xml_files/no_files_2_links_2_textfields.xml
dsp-tools xmlupload --metrics xml_files/no_files_3_links_3_textfields.xml
dsp-tools xmlupload --metrics xml_files/no_files_4_links_4_textfields.xml
dsp-tools xmlupload --metrics xml_files/one_file.xml
```

dsp-tools will then create a metrics report in the folder `metrics`.
