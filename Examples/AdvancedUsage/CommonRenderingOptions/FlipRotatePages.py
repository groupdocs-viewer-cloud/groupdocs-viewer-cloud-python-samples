# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to rotate output pages when viewing a document as PDF
class FlipRotatePages:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "PDF"
        view_options.render_options = groupdocs_viewer_cloud.PdfOptions()
        page_rotation = groupdocs_viewer_cloud.PageRotation()
        page_rotation.page_number = 1
        page_rotation.rotation_angle = "On90Degree"
        view_options.render_options.page_rotations = [page_rotation]

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("FlipRotatePages completed: " + response.file.path)
