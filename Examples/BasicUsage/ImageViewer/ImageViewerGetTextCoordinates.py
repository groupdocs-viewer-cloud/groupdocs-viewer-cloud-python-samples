# Import modules
import groupdocs_viewer_cloud
from Common import Common

# This example demonstrates how to retrieve and print out text with coordinates
class ImageViewerGetTextCoordinates:
    @classmethod  
    def Run(cls):
        apiInstance = groupdocs_viewer_cloud.InfoApi.from_config(Common.GetConfig())
        view_options = groupdocs_viewer_cloud.ViewOptions()
        view_options.file_info = groupdocs_viewer_cloud.FileInfo()
        view_options.file_info.file_path = "SampleFiles/sample.docx"
        view_options.view_format = "PNG"
        view_options.render_options = groupdocs_viewer_cloud.ImageOptions()
        view_options.render_options.extract_text = True       

        request = groupdocs_viewer_cloud.GetInfoRequest(view_options)
        response = apiInstance.get_info(request)
        for i in range(3):
            line = response.pages[0].lines[i]
            print(" x: " + str(line.x) + "; y: " + str(line.y))
        print("ImageViewerGetTextCoordinates completed: " + str(len(response.pages)))
