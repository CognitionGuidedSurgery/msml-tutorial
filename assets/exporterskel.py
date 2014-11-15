from msml.exporter import Exporter

class ExporterSkeleton(Exporter):
    def __init__(self, msmlfile):
        self.initialize(msmlfile, name = "myexporter",
                        features = supported,
                        mesh_sort = ...,
                        output_type_of_elements = ...)

    def render(self):
        self._update = {}
        for sceneobject in self.datamodel:
            # process object
            sceneobject.id
            sceneobject.mesh
            for constraints in sceneobject.constraints:  pass
            for regions in sceneobject.materials: pass
            for output in sceneobject.output: pass

        # write simulation input file

    def execute(self):
        # execute the simulation
        subprocess.call(["run_simulation" ...])
        # return the new memory values
        return self._update
