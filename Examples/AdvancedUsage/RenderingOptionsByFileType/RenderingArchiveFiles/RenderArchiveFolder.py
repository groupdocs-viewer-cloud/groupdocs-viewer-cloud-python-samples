# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render archive folder
class RenderArchiveFolder:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_folders.zip"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.archive_options = groupdocs_viewer_cloud.ArchiveOptions()
        view_options.render_options.archive_options.folder = "ThirdFolderWithItems"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenderArchiveFolder completed: " + str(len(response.pages)))
