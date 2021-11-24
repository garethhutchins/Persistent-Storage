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
http://host/storage/<br />
Accept form data<br />
Create a new save for the model with the following inputs:<br />
{<br />
    'file_name' : 'The name of the file, usually a unique ID',<br />
    'model_type' : 'NMF|LDA|TF-IDF',<br />
    'num_topics' : 'The number of topics used in the model (integer)',<br />
    'normalisation' : 'stemming|lemmitisation|none',<br />
    'topic_labels' : 'A json dictionary of the lables',<br />
    'save_model' : 'A pickle of the saved model and vectoriser'<br />
    'topics_image' : 'An image representation of the top words for each topic'<br />
}

### GET model
Get the model of a specific ID
http://host/storage/{ID}

### Put model
Update a model - generally used for updating the topic images when the topcs have been given a name <br />
{<br />
    'topic_labels' : 'A json dictionary of the lables',<br />
}

### Delete a model
http://host/storage/{ID}
