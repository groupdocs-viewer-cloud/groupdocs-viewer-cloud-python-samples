# Import modules
import groupdocs_viewer_cloud
import os
from Common import Common

# This example demonstrates how to convert and download document without using cloud storage
class ConvertAndDownload:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())

        format = "jpg"      
        file = open("Resources/SampleFiles/sample.docx", "r")

        request = groupdocs_viewer_cloud.ConvertAndDownloadRequest(format, file)

        response = apiInstance.convert_and_download(request)

        print("ConvertAndDownload completed: " + os.path.getsize(response))
