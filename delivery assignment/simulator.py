import random
from models import Package, DeliveryVan
from rich.table import Table
from rich.console import Console

def run_simulation():
    destination = ["Nairobi", "Mombasa", "Kisumu", "Eldoret"]
    packages = []
    results = []

    for i in range(1, 11):
        pkg_id = f"PCK-{str(i).zfill(3)}"
        weight = random.randint(1, 30)
        destination = random.choice(destination)
        pkg = Package(pkg_id, weight, destination)
        packages.append(pkg)

    van = DeliveryVan("Blue Bolt", 100)

    for pkg in packages:
        loaded = van.load_package(pkg)
        status = "Delivered" if loaded else "Skipped"
        results.append({
            "id": pkg.id,
            "destination": pkg.destination,
            "weight":f"{pkg.weight}pounds",
            "status": status
        })
    van.deliver

    console = Console()
    table = Table(title = "ZipZap Express - Delivery Summary")
    table.add_column("Package ID", style="cyan", no_wrap=True)
    table.add_column("Destination", style="magenta")
    table.add_column("Weight", style="green")
    table.add_column("status", style="bold")

    for res in results:
        table.add_row(res["id"], res["destination"], res["weight"], res["status"])

    console.print(table)
