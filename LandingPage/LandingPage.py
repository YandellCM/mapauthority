import reflex as rx

def qr_tracking_section():
    return rx.vstack(
        # Título principal en naranja (nuevo)
        rx.heading(
            "Asset Tracking Infrastructure for Everyone",
            class_name="text-3xl font-bold text-center mb-2 text-orange-500"
        ),
        
        # Subtítulo existente
        rx.heading(
            "Location Tracking with QR Labels",
            class_name="text-2xl font-bold text-center mb-4 text-gray-800"
        ),
        
        # Texto descriptivo
        rx.text(
            "Print your own Asset Tags, attach them to anything you want to track.",
            class_name="text-center text-gray-600 mb-8"
        ),
        
        
        # Divider line
        rx.divider(class_name="my-6 border-gray-300"),
        
        # Early Access button
        rx.center(
            rx.button(
                "Request Early Access →",
                class_name="bg-orange-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors"
            ),
            class_name="mb-10"
        ),
        
        
        # Main image
        rx.center(
            rx.image(
                src="img1.png",
                alt="QR Tracking System",
                class_name="w-full max-w-4xl rounded-lg shadow-md mt-10"
            )
        ),
        
        class_name="space-y-8 p-8 max-w-7xl mx-auto"
    )

def index():
    return rx.container(
        rx.vstack(
            # Header with logo
            rx.hstack(
                rx.image(
                    src="logo.png",
                    alt="Company Logo",
                    class_name="h-12 w-auto"
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link("Features", class_name="text-gray-600 hover:text-gray-900"),
                    rx.link("Pricing", class_name="text-gray-600 hover:text-gray-900"),
                    rx.link("Contact", class_name="text-gray-600 hover:text-gray-900"),
                    class_name="hidden md:flex space-x-8"
                ),
                rx.button("Get Beta Access", class_name="bg-orange-500 text-white px-4 py-2 rounded-lg hover:bg-orange-600"),  # ÚNICO cambio realizado"),
                class_name="w-full py-4 px-6 border-b border-gray-200"
            ),
            
            # Main content
            qr_tracking_section(),
            
            class_name="min-h-screen bg-gray-50"
        )
    )

app = rx.App()
app.add_page(index)