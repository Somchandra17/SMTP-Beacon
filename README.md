# SMTP-Beacon

This Python script checks if the SMTP port 25 is open on a list of IP addresses. It reads IP addresses from a text file and reports whether each IP can be connected to on port 25.

## Requirements

- Python 3.x
- `smtplib` and `socket` libraries (both are included in the Python standard library)

## Installation

1. Clone the repository or download the script file.

2. Ensure you have Python 3.x installed on your system.

## Usage

1. Create a text file containing the list of IP addresses you want to check, with one IP address per line. For example:

    ```
    192.168.1.1
    10.0.0.1
    172.16.0.1
    ```

2. Run the script from the command line, passing the path to your text file as an argument:

    ```sh
    python check_smtp.py path/to/ip_list.txt
    ```

    Replace `path/to/ip_list.txt` with the actual path to your text file.

## Example

Given a text file `ips.txt` with the following content:

```
192.168.1.1
10.0.0.1
172.16.0.1
```


Run the script:

```sh
python check_smtp.py ips.txt
```

Output:

```
192.168.1.1: Open
10.0.0.1: Closed
172.16.0.1: Open
```


