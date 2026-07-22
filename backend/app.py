from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

vendors = [
    {
        "id": 'ab95f455-313e-4821-888c-a99bb0b72208',
        "name": "TechHub Nepal",
        "address": "New Road, Kathmandu",
        "discount": "10%"
    },
    {
        "id": '918fbce1-10af-4244-882a-fe7d1a5ae369',
        "name": "Pokhara Fashion House",
        "address": "Lakeside, Pokhara",
        "discount": "10%"
    },
    {
        "id": '8786107e-02f7-4d36-a701-12fa7afdc619',
        "name": "Healthy Life Pharmacy",
        "address": "Pulchowk, Lalitpur",
        "discount": "10%"
    },
]

# Get all vendors
@app.route("/vendors", methods=["GET"])
def get_vendors():
    return jsonify(vendors)

# Get single vendor by id
@app.route("/vendors/<vendor_id>", methods=["GET"])
def get_vendor(vendor_id):
    for vendor in vendors:
        if vendor["id"] == vendor_id:
            return jsonify(vendor)

    return jsonify({
        "error": "Vendor not found"
    }), 404

# Add vendor
@app.route("/vendors", methods=["POST"])
def add_vendor():
    data = request.json
    vendor = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "address": data.get("address"),
        "discount": data.get("discount")
    }
    vendors.append(vendor)
    return jsonify({
        "message": "Vendor added",
        "vendor": vendor
    }), 201

# Get coupon discount
@app.route("/vendors/<vendor_id>/coupon/<code>", methods=["GET"])
def get_coupon(vendor_id, code):

    for vendor in vendors:
        if vendor["id"] == vendor_id:
            discount = vendor["discount"]
            if discount:
                return jsonify({
                    "discount": discount
                })
            return jsonify({
                "error": "Coupon not found"
            }), 404
    return jsonify({
        "error": "Vendor not found"
    }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5555, debug=True)