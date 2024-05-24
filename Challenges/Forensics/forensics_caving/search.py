import os
from collections import OrderedDict
from Evtx.Evtx import Evtx
from bs4 import BeautifulSoup


def process_evtx_files(directory, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(f"<Events>\n")
        # outfile.write(f"processing EVTX files in {directory}")
        for filename in os.listdir(directory):
            if filename.endswith(".evtx"):
                evtx_path = os.path.join(directory, filename)
                outfile.write(f'<File filename="{filename}">\n')
                # outfile.write(
                #     f"processing {directory}\{filename}\n*****************************************************\n\n"
                # )

                with Evtx(evtx_path) as log:
                    # header = log.get_file_header()
                    # properties = OrderedDict(
                    #     [
                    #         ("major_version", "File version (major)"),
                    #         ("minor_version", "File version (minor)"),
                    #         ("is_dirty", "File is dirty"),
                    #         ("is_full", "File is full"),
                    #         ("next_record_number", "Next record number"),
                    #     ]
                    # )
                    # for key, value in properties.items():
                    #     outfile.write(f"{value}: {getattr(header, key)()}\n")

                    # outfile.write("\n")
                    for record in log.records():
                        xml = record.xml()
                        outfile.write(xml)
                        # event_details = extract_event_details(xml)
                        # outfile.write(event_details)
                    # outfile.write(
                    # "----------------------------------------------------------------------------------------------\n\n"
                    # )
                outfile.write(f"</File>\n")
        outfile.write(f"</Events>\n")


def extract_event_details(xml):
    soup = BeautifulSoup(xml, "xml")
    log_name = soup.find("Channel").text if soup.find("Channel") else "N/A"
    event_id = soup.find("EventID").text if soup.find("EventID") else "N/A"
    timestamp = (
        soup.find("TimeCreated")["SystemTime"] if soup.find("TimeCreated") else "N/A"
    )
    message = (
        soup.find("Message").text if soup.find("Message") else "No message available"
    )

    details = (
        f"Log Name: {log_name}\n"
        f"Event ID: {event_id}\n"
        f"Timestamp: {timestamp}\n"
        f"Message: {message}\n\n"
    )
    return details


if __name__ == "__main__":
    evtx_directory = "D:\\Users\\curtismechling\\Documents\\CTFs\\Hack The Box\\Business CTF 2024\\Forensics\\forensics_caving\\Logs"
    output_file = "D:\\Users\\curtismechling\\Documents\\CTFs\\Hack The Box\\Business CTF 2024\\Forensics\\forensics_caving\\evtx_output.xml"
    process_evtx_files(evtx_directory, output_file)
