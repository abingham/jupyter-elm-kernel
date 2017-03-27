from ipykernel.kernelbase import Kernel
import os
import subprocess
from tempfile import TemporaryDirectory


class ElmKernel(Kernel):
    implementation = 'Elm'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {'mimetype': 'text/html'}
    banner = "Display Elm output"

    def do_execute(self, code, silent,
                   store_history=True,
                   user_expressions=None,
                   allow_stdin=False):
        # if not silent:
        #    stream_content = {'name': 'stdout', 'text': code}
        #    self.send_response(self.iopub_socket, 'stream', stream_content)

        with TemporaryDirectory() as tmpdirname:
            infile = os.path.join(tmpdirname, 'input.elm')
            outfile = os.path.join(tmpdirname, 'index.html')

            with open(infile, mode='wt') as f:
                f.write(code)
            #  TODO: Deal with exceptions from this call
            subprocess.run(['elm-make', infile, '--yes',
                            '--output={}'.format(outfile)],
                           cwd=tmpdirname,
                           check=True)

            with open(outfile, mode='rt') as f:
                html = f.read()

        display_content = {'name': 'stdout',
                           'source': 'Elm',
                           'data': {'text/html': html}}
        self.send_response(self.iopub_socket, 'display_data', display_content)

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
