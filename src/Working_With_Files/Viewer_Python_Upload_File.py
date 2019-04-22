# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities

class Viewer_Python_Upload_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_viewer_cloud.UploadFileRequest("viewerdocs\\one-page.docx", "D:\\ewspace\\GroupDocs.Viewer.Cloud.Python.Examples\\src\\Resources\\viewerdocs\\one-page.docx", Common_Utilities.myStorage)
            response = api.upload_file(request)
            
            print("Expected response type is FilesUploadResult: " + str(response))
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))