---
layout: workshop
title: "Bootcamp: Learning representations of text for NLP"
subtitle: Learn and implement an end-to-end deep learning models for natural language processing.
datelocation: "19-20 May 2018, 09:00 AM - 05:00 PM, ThoughtFactory, Bangalore"
city: Bangalore
start_time: 2018-05-19
end_time: 2018-05-20
description: "Learn and implement an end-to-end deep learning models for natural language processing."
boxoffice_item_collection: '761d606f-7c46-4926-b920-1386824de2e7'

venue:
  label: ThoughtFactory, Bangalore
  address: |
    ThoughtFactory,
    Tower D, 2nd Floor,
    Diamond District, Bengaluru, Karnataka 560102
  lat: 12.95921
  lng: 77.64431
  google_maps_url: https://goo.gl/maps/eaNceNnatu62

instructors:
- name: Anuj Gupta
  byline: Director - Machine Learning, Huawei Technologies
  image_url: https://images.hasgeek.com/embed/file/a524455ee6b34301aaaa4faa31a2564a
  website:
    url: https://www.linkedin.com/in/anuj-gupta-15585792/
    label: Linkedin
  bio: |
    **Anuj** is a seasoned ML researcher; working in the area NLP, Machine Learning, Deep learning. Currently he is heading ML/DL efforts for Huawei India R&D. Prior to this he was heading ML efforts at Freshworks and Airwoot(Now acquired by Freshdesk). He dropped out of Phd in ML to work with startups. He graduated from IIIT H with specialization in theoretical comp science. He has authored a bunch of research publications and patents. He is a regular speaker at prestigious forums like PyData, Anthill, The Fifth Elephant, NVidia Dev conf, conferences in distributed algorithms. He is also co-organizer of special interest groups like DLBLR.
- name: Satyam Saxena
  byline: Applied Scientist - Machine Learning, Amazon
  image_url: https://images.hasgeek.com/embed/file/4727b3dd37aa4880a7d87f03056f7727
  website:
    url: https://www.linkedin.com/in/sam-iitj/
    label: Linkedin
  bio: |
    **Satyam** is a ML scientist working in the area of Deep learning, NLP and Machine Learning. Currently, he is leading various efforts in the area of machine learning and analytics at Amazon. Prior to this he was a ML researcher at Freshdesk, before which he was also part of the core ML group at Cisco Security. He was also a visiting researcher at Vision Labs in IIIT Hyd where he used computer vision and deep learning to build applications to assisting visually impaired people. He presented some of this work at ICAT 2014, Turkey.
overview:
  left_content: |
    Think of your favorite NLP application that you wish to build - sentiment analysis, named entity recognition, machine translation, information extraction, summarization, recommender system, to name a few. A key step towards achieving any of the above task is - using the right set of techniques to represent text in a form that machine can easily understand.
    
    Unlike images, where directly using the intensity of pixels is a natural way to represent the image; in case of text there is no such natural representation. No matter how good is your ML algorithm, it can do only so much unless there is a richer way to represent underlying text data. Thus, whatever NLP application you are building, it’s imperative to find a good representation for your text data. Motivated from this, the subfield of  representation learning of text for NLP has attracted a lot of research interest in the past few years.
    
    In this bootcamp, we will understand key concepts, maths, and code behind the state-of-the-art techniques for text representation. Various representation learning techniques have been proposed in literature, but still there is a dearth of comprehensive tutorials that provides full coverage with mathematical explanations as well as implementation details of these algorithms to a satisfactory depth.
    
    This bootcamp aims to bridge this gap. It aims to demystify, both - Theory (key concepts, maths) and Practice (code) that goes into building these representation schemes. At the end of this bootcamp participants would have gained a fundamental understanding of these schemes with an ability to implement them on datasets of their interest.


    # Target Audience
    
    * Machine learning practitioners
    * Anyone (researcher, student, professional) learning NLP
    * Corporates and Start-ups looking to add NLP to their product or service offerings


    # Pre-requisites

    * This is a hands-on course and hence, participants should be comfortable with programming. Familiarity with python data stack is ideal.
    * Prior knowledge of machine learning will be helpful. Participants should have some practice with basic NLP problems e.g. sentiment analysis.
    * While the DL concepts will be taught in an intuitive way, some prior knowledge of linear algebra and probability theory would be helpful.


    # Resources

    The material for the bootcamp is hosted on [github](https://github.com/anujgupta82/Representation-Learning-for-NLP). You can find slides for this workshop [here](https://www.slideshare.net/anujgupta5095/representation-learning-of-text-for-nlp).
  
    This is from the popular bootcamp series by the speakers on NLP. Additional materials relevant would be shared prior to the bootcamp.

  right_content: |
    # Approach
    
    This would be a two-day instructor-led hands-on bootcamp to learn and implement an end-to-end deep learning models for natural language processing.

      * Day1 will cover introduction to text representation, old ways of representing text, followed by a deep dive into embedding spaces and word vectors.
      * Day2 will cover more advanced techniques of representing text such as Paragraph2vec/doc2vector techniques and various architectures for char2vec.
    
    There will be  four  sessions of  three  hours each over two days .
    
    #### Session 1: Introduction to representation learning
            
    1. What is representation learning?
    2. Use cases in natural language processing.
    3. Old ways of representing text
      * One-hot encoding
      * Tf-idf
      * N-grams
    4. How to use pre-trained word embedding?

    #### Session 2: Word-vectors
            
    1. Introduction to word-vectors?
    2. Different techniques of generating word-vectors
      * CBOW, Skip-gram model
      * Glove model
    3. Detailed implementation of each of these models in tensorflow 
    4. Negative sampling, hierarchical softmax, tSNE
    5. Fine-tuning pretrained embeddings
    
    #### Session 3: Sentence2vec/Paragraph2vec/Doc2vec
           
    1. Extending word vectors to represent sentences/paragraphs/documents
    2. Various techniques for training doc2vec 
      * Doc2vec
        i. DM
        ii. DBOW 
      * Skip - thoughts
    3. Detailed implementation of each of these models in tensorflow
    
    #### Session 4: Char2vec

    1. Building character embeddings
    2. Tweet2vec - character embeddings from social data
    3. CNN for character vectors.
    4. fastText - character n-gram embeddings

    # Software Requirements
    
    We will be using Python data stack for the bootcamp with keras and tensorflow for the deep learning component. Please install Anaconda for Python 3 for the bootcamp. Additional requirement will be communicated to participants.
---
