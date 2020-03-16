# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render password-protected documents
class ViewProtectedDocument:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/password_protected.docx"
        view_options.file_info.password = "12345"
        view_options.view_format = "HTML"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("ViewProtectedDocument completed: " + str(len(response.pages)))
