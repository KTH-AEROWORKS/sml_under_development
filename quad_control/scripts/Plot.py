#!/usr/bin/env python

import missions.missions_database
MISSIONS_DATABASE = missions.missions_database.database2

from utilities import jsonable

import matplotlib
# this is necessary because of threading and plotting
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import matplotlib.backends.backend_pdf

import pdfkit

from PyPDF2 import PdfFileMerger, PdfFileReader 

DATA_FILE = "/home/pedrootao/SML_CODE/src/quad_control/experimental_data/data/_1466514457_aaaaaaaaaaaaaaa.txt"


def handle_plot_service():

    data_file = DATA_FILE

    # read mode by default
    read_file = open(data_file).read()

    read_file = read_file.split(jsonable.Jsonable.UNIQUE_STRING)

    read_file.pop(0)

    merger = PdfFileMerger()

    while len(read_file) >= 1:
        description = read_file.pop(0)

        name, constructing_string = jsonable.Jsonable.inverse_parametric_description(description)

        data = read_file.pop(0)

        MissionClass   = MISSIONS_DATABASE[name]
        mission_active = MissionClass.from_string(constructing_string)

        mission_description = mission_active.object_combined_description()

        pdfkit.from_string(mission_description, data_file[:-4]+".pdf")
        merger.append(PdfFileReader(file(data_file[:-4]+".pdf","rb")))

        fig = plt.figure()
        pdf = matplotlib.backends.backend_pdf.PdfPages(data_file[:-4]+".pdf")

        for fig in mission_active.plot_from_string(data):
            pdf.savefig(fig)

        plt.close("all")
        pdf.close()

        merger.append(PdfFileReader(file(data_file[:-4]+".pdf","rb")))

    merger.write(data_file[:-4]+".pdf")

    return "Done"

handle_plot_service()    