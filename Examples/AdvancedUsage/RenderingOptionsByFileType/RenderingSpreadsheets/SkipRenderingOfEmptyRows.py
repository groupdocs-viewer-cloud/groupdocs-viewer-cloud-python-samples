# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to omit to render empty rows
class SkipRenderingOfEmptyRows:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_empty_row.xlsx"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.spreadsheet_options = groupdocs_viewer_cloud.SpreadsheetOptions()    
        view_options.render_options.spreadsheet_options.render_empty_rows = False

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("SkipRenderingOfEmptyRows completed: " + str(len(response.pages)))
