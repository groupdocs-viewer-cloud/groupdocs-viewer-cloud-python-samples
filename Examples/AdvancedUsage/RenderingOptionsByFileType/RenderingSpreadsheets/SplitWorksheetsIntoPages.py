# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to split worksheets into pages
class SplitWorksheetsIntoPages:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.xlsx"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.spreadsheet_options = groupdocs_viewer_cloud.SpreadsheetOptions()    
        view_options.render_options.spreadsheet_options.paginate_sheets = True
        view_options.render_options.spreadsheet_options.count_rows_per_page = 45

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("SplitWorksheetsIntoPages completed: " + str(len(response.pages)))
