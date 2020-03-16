# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to render only the print areas from worksheets
class RenderPrintAreas:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/with_four_print_areas.xlsx"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.spreadsheet_options = groupdocs_viewer_cloud.SpreadsheetOptions()    
        view_options.render_options.spreadsheet_options.render_print_area_only = True

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenderPrintAreas completed: " + str(len(response.pages)))
