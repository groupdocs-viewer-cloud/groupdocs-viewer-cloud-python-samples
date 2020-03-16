# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render a Word document including tracked changes
class RenderTrackedChanges:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_tracked_changes.docx"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.word_processing_options = groupdocs_viewer_cloud.WordProcessingOptions()    
        view_options.render_options.word_processing_options.render_tracked_changes = True

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenderTrackedChanges completed: " + str(len(response.pages)))
