Dataverse Display of Quality
============================

Experiments that try to display quality 'label' information on the Dataverse archive front-end. 

Using the custom-footer.html we can inject javascript code that will try to find quality data with datasets and display that next to or near the other dataset information. 

In order to demonstrate this you must have access to a Dataverse installation and be able to change the custom footer setting and provide that file. 

Instructions for DANS developers with access to on the `dans-core-systems` repo:
1. Get into the repo directory (assuming you have everything in place for the standard development). 
2. Copy the custom footer file into the `shared` dir. 
3. SSH into the dev box with vagrant
4. Set the custom footer to point to that `/vagrant/shared` folder: `curl -X PUT -d '/vagrant/shared/custom-footer.html' http://localhost:8080/api/admin/settings/:FooterCustomizationFile`. 


## Initial experiment

Without 'connecting' to a service, we just generate random quality percentages. 
When the value is lower than 50% we ignore it and do not show the label. This 50% is kind of arbitrary and we might consider a different value, maybe even 0% effectively showing all.
The position, 'style' and content (text in this case) of the label is kept very simple, but could be changed.  

Screenshot of the Datastation with a search result page, showing the quality.  
![test-searchresult-page](./Screenshot%20from%202025-10-21%2015-04-36.png)

Screenshot of the Datastation with a Dataset 'landing' page, showing the quality. 
![test-datasetlanding-page](./Screenshot%20from%202025-10-21%2015-05-24.png)



