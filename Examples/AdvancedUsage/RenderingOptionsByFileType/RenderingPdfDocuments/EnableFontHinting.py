# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to adjust the display of an outline font
class EnableFontHinting:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.ViewApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.pdf"
        view_options.view_format = "PNG"
        view_options.render_options = groupdocs_viewer_cloud.ImageOptions()
        view_options.render_options.pdf_document_options = groupdocs_viewer_cloud.PdfDocumentOptions()    
        view_options.render_options.pdf_document_options.enable_font_hinting = True

        request = groupdocs_viewer_cloud.CreateViewRequest(view_options)
        response = apiInstance.create_view(request)
        print("EnableFontHinting completed: " + str(len(response.pages)))
