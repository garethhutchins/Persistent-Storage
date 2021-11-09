# Persistent-Storage
Persistent Storage for trained models for the narrative flow analyser to use.

## Supported Actions
The following are the supported actions that the service handles
### GET
Get a list of models and their attributes<br />
{<br />
    "file_name": "",<br />
    "model_type": "",<br />
    "num_topics": null,<br />
    "normalisation": "",<br />
    "topic_labels": null,<br />
    "save_model": null<br />
}
### POST
http://host/storage/
Accept form data<br />
Create a new save for the model with the following inputs:<br />
{<br />
    'file_name' : 'The name of the file, usually a unique ID',<br />
    'model_type' : 'NMF|LDA|TF-IDF',<br />
    'num_topics' : 'The number of topics used in the model (integer)',<br />
    'normalisation' : 'stemming|lemmitisation|none',<br />
    'topic_labels' : 'A json dictionary of the lables',<br />
    'save_model' : 'A pickle of the saved model and vectoriser'<br />
}

###GET model
Get the model of a specific ID
http://host/storage/{ID}

###Delete a model
http://host/storage/{ID}
