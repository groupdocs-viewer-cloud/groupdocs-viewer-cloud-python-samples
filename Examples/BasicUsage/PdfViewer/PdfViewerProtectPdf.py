# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to protect output PDF document
class PdfViewerProtectPdf:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "PDF"
        view_options.render_options = groupdocs_viewer_cloud.PdfOptions()
        view_options.render_options.permissions = ["DenyModification"]
        view_options.render_options.permissions_password = "p123"
        view_options.render_options.document_open_password = "o123"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("PdfViewerProtectPdf completed: " + response.file.path)
