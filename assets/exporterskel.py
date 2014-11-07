from msml.exporter import Exporter

class ExporterSkeleton(Exporter):
    def __init__(self, msmlfile):
        self.initialize(msmlfile, name = "myexporter",
                        features = supported,
                        mesh_sort = ...,
                        output_type_of_elements = ...)

    def render(self):
        #
        #
        #
        #
        pass

    def execute(self):
        #
        #
        #
        #
        pass
