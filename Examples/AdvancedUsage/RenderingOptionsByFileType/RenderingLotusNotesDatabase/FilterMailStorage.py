# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to to filter Lotus Notes database messages
class FilterMailStorage:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.nsf"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.mail_storage_options = groupdocs_viewer_cloud.MailStorageOptions()    
        view_options.render_options.mail_storage_options.text_filter = "April 2015"
        view_options.render_options.mail_storage_options.address_filter = "test@test.com"

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("FilterMailStorage completed: " + str(len(response.pages)))
