import click
from rigel.cli.command import CLICommand
from rigel.exceptions import RigelError
from rigel.loggers import get_logger
from rigel.orchestrator import Orchestrator
from sys import exit

LOGGER = get_logger()


class RunJobCommand(CLICommand):
    """Run a job or sequence of jobs
    """

    def __init__(self) -> None:
        super().__init__(command='run')

    @click.command()
    @click.argument('job', type=str)
    @click.option('--file', '-f', 'file', type=str, required=False,
        default='./Rigelfile',
        show_default=False,
        help='Path to Rigelfile'
    )
    def job(self, job: str, file: str) -> None:
        """Run a single job
        """
        try:
            orchestrator = Orchestrator(file)
            orchestrator.run_job(job)
        except RigelError as err:
            LOGGER.error(err)
            exit(1)

    @click.command()
    @click.argument('sequence', type=str)
    @click.option('--file', '-f', 'file', type=str, required=False,
        default='./Rigelfile',
        show_default=False,
        help='Path to Rigelfile'
    )
    def sequence(self, sequence: str, file: str) -> None:
        """Run a sequence of jobs
        """
        try:
            orchestrator = Orchestrator(file)
            orchestrator.run_sequence(sequence)
        except RigelError as err:
            LOGGER.error(err)
            exit(1)
