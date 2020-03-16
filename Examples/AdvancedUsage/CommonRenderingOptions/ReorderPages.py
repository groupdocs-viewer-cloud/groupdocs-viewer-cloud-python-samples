# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to reorder pages
class ReorderPages:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        # Pass page numbers in the order you want to render them
        view_options.render_options.pages_to_render = [2, 1]

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("ReorderPages completed: " + str(len(response.pages)))
