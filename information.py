# -*- coding:utf-8 -*-

class Information:
    def __init__(self, iid, typel, title, author, corauthor, dates, disease, symptom, acupoint, location, annotation, writer):
        self.iid = iid
        self.typel = typel
        self.title = title
        self.author = author
        self.corauthor = corauthor
        self.dates = dates
        self.disease = disease
        self.symptom = symptom
        self.acupoint = acupoint
        self.location = location
        self.annotation = annotation
        self.writer = writer


class Acupoint:
    def __init__(self, id, chinese, vein, dissection, disease, compatibility, location, url):
        self.id = id
        self.chinese = chinese
        self.vein = vein
        self.dissection = dissection
        self.disease = disease
        self.compatibility = compatibility
        self.location = location
        self.url = url