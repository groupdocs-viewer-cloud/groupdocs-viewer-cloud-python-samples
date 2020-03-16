# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render consecutive pages
class RenderConsecutivePages:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.start_page_number = 1
        view_options.render_options.count_pages_to_render = 2

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenderConsecutivePages completed: " + str(len(response.pages)))
