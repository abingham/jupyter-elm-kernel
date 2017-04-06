from ipykernel.kernelbase import Kernel
import os
import subprocess
from tempfile import TemporaryDirectory


class ElmKernel(Kernel):
    implementation = 'elm_kernel'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'name': 'elm',
                     'codemirror_mode': 'elm',
                     'mimetype': 'text/x-elm',
                     'file_extension': '.elm'}
    banner = "Display Elm output"

    def do_execute(self, code, silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):
        with TemporaryDirectory() as tmpdirname:
            infile = os.path.join(tmpdirname, 'input.elm')
            outfile = os.path.join(tmpdirname, 'index.js')

            with open(infile, mode='wt') as f:
                f.write(code)

            #  TODO: Deal with exceptions from this call
            subprocess.run(['elm-make', infile, '--yes',
                            '--output={}'.format(outfile)],
                           cwd=tmpdirname,
                           check=True)

            with open(outfile, mode='rt') as f:
                javascript = f.read()

        javascript = javascript + "; var mountNode = document.getElementById('elm-div'); Elm.Main.embed(mountNode);"

        self.send_response(
            self.iopub_socket,
            'display_data',
            {
                'metadata': {},
                'data': {
                    'text/html': '<div id="elm-div"></div>'
                }
            }
        )

        self.send_response(
            self.iopub_socket,
            'display_data',
            {
                'metadata': {},
                'data': {
                    'application/javascript': javascript
                }
            })

        # self.send_response(
        #     self.iopub_socket,
        #     'display_data',
        #     {
        #         'metadata': {},
        #         'data': {
        #             'application/javascript': 'var mountNode = document.getElementById("elm-div"); Elm.Main.embed(mountNode);'
        #         }
        #     }

        # )

        return {
            'status': 'ok',
            # The base class increments the execution count
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }


if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=ElmKernel)
