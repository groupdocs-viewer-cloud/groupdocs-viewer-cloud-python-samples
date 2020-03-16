# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to get document info
class GetDocumentInformation:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_viewer_cloud.InfoApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"

        request = groupdocs_viewer_cloud.GetInfoRequest(view_options)
        result = infoApi.get_info(request)
        print("GetDocumentInformation completed: " + str(len(result.pages)))