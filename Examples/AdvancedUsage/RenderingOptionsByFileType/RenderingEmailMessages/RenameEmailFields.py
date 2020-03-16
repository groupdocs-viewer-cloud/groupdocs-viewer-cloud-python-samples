# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to use custom field labels
class RenameEmailFields:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.msg"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.email_options = groupdocs_viewer_cloud.EmailOptions()
        field_label1 = groupdocs_viewer_cloud.FieldLabel()
        field_label1.field = "From"
        field_label1.label = "Sender"
        field_label2 = groupdocs_viewer_cloud.FieldLabel()
        field_label2.field = "To"
        field_label2.label = "Receiver"        
        view_options.render_options.email_options.field_labels = [field_label1, field_label2]

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("RenameEmailFields completed: " + str(len(response.pages)))
