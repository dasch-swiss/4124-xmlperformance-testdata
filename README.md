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


## Steps to do performance measures

First, create the project `xmlperformance` with 

```
dsp-tools create xmlperformance.json
```

Then, upload the data file with

```
dsp-tools xmlupload xmlperformance.xml
```
