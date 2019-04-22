# Import modules
import groupdocs_viewer_cloud
from Common_Utilities.Utils import Common_Utilities


class Viewer_Python_Get_Info_With_SpreadsheetOptions:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_ViewerApi_Instance()
        
        try:
            viewOptions = groupdocs_viewer_cloud.ViewOptions()

            fileInfo = groupdocs_viewer_cloud.FileInfo()
            fileInfo.file_path = "viewerdocs\\with-hidden-rows-and-columns.xlsx"
            fileInfo.password = ""
            fileInfo.storage_name = Common_Utilities.myStorage
        
            viewOptions.file_info = fileInfo;
            
            renderOptions = groupdocs_viewer_cloud.RenderOptions()
            
            spreadsheetOptions = groupdocs_viewer_cloud.SpreadsheetOptions()
            spreadsheetOptions.paginate_sheets = True
            spreadsheetOptions.count_rows_per_page = 5
        
            renderOptions.spreadsheet_options = spreadsheetOptions
            viewOptions.render_options = renderOptions
        
            request = groupdocs_viewer_cloud.GetInfoRequest(viewOptions)
            response = api.get_info(request)
        
            print("Expected response type is InfoResult: " + str(response))
        except groupdocs_viewer_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))