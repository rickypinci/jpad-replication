# Replication Package: Automated Detection of Software Performance Antipatterns in Java-based Applications

This is a replication package for the paper titled "Automated Detection of Software Performance Antipatterns in Java-based Applications" and submitted for revision.



## Authors
Catia Trubiani - Gran Sasso Science Institute (Italy)<br/>Riccardo Pinciroli - Gran Sasso Science Institute (Italy)<br/>Andrea Biaggi - University of Milan-Bicocca (Italy)<br/>Francesca Arcelli Fontana - University of Milan-Bicocca (Italy)



## Abstract
The detection of performance issues in Java-based applications is not trivial since many factors concur to poor performance and software engineers are not sufficiently supported for this task.
The goal of this manuscript is to automate the detection of performance problems in running systems to guarantee no quality-based hinders prevent their successful usage.
Using software performance antipatterns, i.e., bad practices expressing both the problem and the solution with the purpose of identifying shortcomings and promptly fixing them, we develop a framework which automatically detects five software antipatterns capturing a variety of performance issues in Java-based applications.
Our approach is applied to five real-world case studies from different domains. As empirical evidence, we show that solving one of the detected antipatterns improves the system performance up to 50%.

A high-level view of the workflow of our approach is presented in the following. The content of this replication package is highlighted by the dashed rectangle.

![High-level workflow of our approach](https://github.com/rickypinci/jpad-replication/blob/main/resources/pad-workflow.png?raw=true)



## Available Files
- *JPAD-0.0.1.jar* is the tool developed for this paper. See [Run JPAD](#run-jpad) for instructions on how to run JPAD.
- *reading_files.zip* contains all the reading files and usage statistics obtained by profiling the five Java applications. After extracting the files, two folders are available: <tt>original/</tt> contains the data profiled from original systems, while <tt>refactored/</tt> contains the reading files of refactored systems (i.e., OpenMRS)
- From <tt>original/</tt> and <tt>refactored/</tt> folders, reading files can be retrieved at <tt>\<load\>-\<duration\>/\<system\>/</tt>, where <tt>\<load\></tt>=(25, 50, 75, 100), <tt>\<duration\></tt>=(3, 6, 12), and <tt>\<system\></tt>=(petclinic, broadleaf, webgoat, ts-security-service, openmrs). Available files are:
	- <tt>Call-tree---All-threads-merged.xml</tt> shows a top-down call tree of all application threads merged together into a single tree.
	- <tt>Call-tree---By-thread.xml</tt> shows an individual top-down call tree for each application thread.
	- <tt>Chart--CPU-Usage.csv</tt> measures the percentage of CPU used during the execution of the application.
	- <tt>Chart--Heap-Memory.csv</tt> measures the percentage of memory used during the execution of the application.
	- <tt>CPU-hot-spots.xml</tt> collects methods which spend the longest time on the CPU.
	- <tt>Method-list--allocations.csv</tt>
	- <tt>Method-list--CPU.csv</tt>
	- <tt>Monitor-usage-statistics.xml</tt>
- The <tt>analysis/</tt> folder contains three files:
	- <tt>original.csv</tt> provides results obtained by running JPAD with the original systems (i.e., PetClinic, Broadleaf, WebGoat, ts-security-service, OpenMRS)
	- <tt>refactored.csv</tt> provides results obtained by running JPAD with the refactored systems (i.e., OpenMRS)
	- <tt>analysis.ipynb</tt> is an iPython Notebook that allows analyzing the two CSV files contained in this directory and generating some figures.



## Prerequisites
- [JDK 11 (or later)](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)
- [JavaFX SDK](https://gluonhq.com/products/javafx/)
<!--- To profile each system while running load tests, it is also necessary to download:-->
<!--	- [YourKit](https://www.yourkit.com/java/profiler/features/)-->
<!--	- [Locust](https://locust.io/)-->
<!--	- The five Java-based applications analyzed in the paper:-->
<!--		- [PetClinic](https://github.com/spring-projects/spring-petclinic)-->
<!--		- [Broadleaf](https://github.com/BroadleafCommerce/DemoSite)-->
<!--		- [WebGoat](https://github.com/WebGoat/WebGoat)-->
<!--		- [TrainTicket](https://github.com/FudanSELab/train-ticket)-->
<!--		- [OpenMRS](https://github.com/openmrs/openmrs-core)-->



## Run JPAD
1) Start JPAD using the command: <tt>java --module-path /\<path\>/\<to\>/openjfx/lib/ --add-modules javafx.controls,javafx.fxml -jar JPAD-0.0.1.jar</tt>.
2) Use the first file picker to select a <tt>CPU-hot-spots.xml</tt>.
3) Use the second file picker to select all the remaining reading files.
4) Choose which software performance antipatterns must be detected and provide the required thresholds. Note that all threshold values are mandatory when the respective antipattern is selected.
5) Press the <tt>Start Analysis</tt> button.

