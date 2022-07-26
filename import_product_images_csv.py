import base64
import csv
import argparse

parser = argparse.ArgumentParser(description='Open CSV file with columns ...')
parser.add_argument('in_file_path', type=str,
                    help='Path to the CSV file containing ID, name and image file path accessible by this script')
parser.add_argument('out_file_path', type=str,
                    help='Path for the output CSV with the base64')
args = parser.parse_args()

new_csv_contents = []

# open file
with open(args.in_file_path) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        product_id, product_name, product_file_path = row

        # open image and convert it to base64
        try:
            with open(product_file_path, 'rb') as image:
                image_base64 = image.read().encode("base64")
        except IOError:
            print("Could not find the image '%s' - please make sure it is accessible to this script" %
                  product_file_path)

        new_csv_contents.append([product_id, product_name, image_base64])

# save
with open(args.out_file_path, 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in new_csv_contents:
        writer.writerow(row)
