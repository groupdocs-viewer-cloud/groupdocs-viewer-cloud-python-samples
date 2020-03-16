# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to adjust image quality when rendering PDF to HTML
class AdjustImageQuality:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.pdf"
        view_options.view_format = "HTML"
        view_options.render_options = groupdocs_viewer_cloud.HtmlOptions()
        view_options.render_options.pdf_document_options = groupdocs_viewer_cloud.PdfDocumentOptions()    
        view_options.render_options.pdf_document_options.image_quality = "Medium"        

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("AdjustImageQuality completed: " + str(len(response.pages)))
