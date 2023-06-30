# from django.shortcuts import render


# # Create your views here.

# def front(request):
#     context = { }
#     return render(request, "index.html", context)

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserAvatarSerializer
from joblib import dump, load

import logging

import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt

# rhea trying
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger("django.request")
logging.warning("WARNING: core.views : logging is active")

class UserAvatarUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserAvatarSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
@api_view(['GET', 'POST'])
def api_add(request):
    sum = 0
    response_dict = {}
    if request.method == 'GET':
        # Do nothing
        pass
    elif request.method == 'POST':
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
    return Response(response_dict, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def api_create_predict(request):
    
    if request.method == 'GET': 
        create_prediction_model()
        pass
    elif request.method == 'POST':
        # Add the numbers
        data = request.data
        
    # return Response("<p>Hello</p>", status=status.HTTP_201_CREATED)
    return Response("test1", status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def api_predict(request):
    logging.warning("core.views : called api predict")
    v1 = "Get Failed"
    v2 = "Post Failed"
    returnValue = []
    if request.method == 'GET': 
        logging.warning("core.views : called GET")
        image_path = 'core/components/strip.jpg'
        returnValue = create_prediction_model(image_path)
        v1 = "Get Called"
        pass
    elif request.method == 'POST':
        logging.warning("core.views : called POST")
        v2 = "Post Called"
        image_path = 'core/components/strip.jpg'
        
        returnValue = create_prediction_model(image_path)
        data = request.data
        
    # return Response("<p>Hello</p>", status=status.HTTP_201_CREATED)
    logging.warning("core.views : called response " + get_RGBlist_as_string(returnValue))
    return Response(v1 + " - " + v2 + "\n" + get_RGBlist_as_string(returnValue), status=status.HTTP_201_CREATED)
    

    
    
    

def generate_colors_from_image(image_path, num_colors):
    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Resize the image for faster processing (optional)
    resized_image = cv2.resize(image, (200, 200))

    # Reshape the image to a flat list of pixels
    pixels = resized_image.reshape(-1, 3)

    # Randomly sample colors from the image pixels
    sampled_indices = np.random.choice(pixels.shape[0], num_colors, replace=False)
    sampled_colors = pixels[sampled_indices]

    return sampled_colors.tolist()




def create_prediction_model(image_path):
    estimator_rf = "Prediction Function Called"
    dump(estimator_rf, 'Urine-Prediction.log')
    loaded_classifier = load('Urine-Prediction.log')
    
    df=pd.read_csv('core/components/ColorChecker30.csv')
    
    # Provide the path to your JPEG image
    
    # image_path = 'core/component/strip.jpg'

    # Generate 10 colors from the image
    urine_colors = generate_colors_from_image(image_path, 10)

    # Print the generated colors
    for color in urine_colors:
        print(color)
        
    return urine_colors


def get_RGBlist_as_string(rgbColorslist):

    strRGB = "["

    i = 0    
    for rgb in rgbColorslist:
        i = i + 1        
        strRGB += "[" 
        j = 0        
        for color in rgb:
            j = j + 1
            strRGB += str(color) 
            if j != 3:             
                strRGB += "," 
        if i != 10:        
            strRGB += "], "
        else:
             strRGB += "] "
    strRGB += "]"
    return strRGB
        