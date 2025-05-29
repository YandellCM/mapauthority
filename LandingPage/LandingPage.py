import reflex as rx

def index():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.hstack(
                    rx.image(
                        src="imglogoten.png",
                        alt="MapAuthority Logo",
                        class_name="h-10 w-auto ml-4 mr-8"
                    ),
                    rx.hstack(
                        rx.link("Overview", href="#", class_name="text-gray-300 hover:text-white transition-colors whitespace-nowrap"),
                        rx.link("Pricing", href="#", class_name="text-gray-300 hover:text-white transition-colors whitespace-nowrap"),
                        rx.link("Blog", href="#", class_name="text-gray-300 hover:text-white transition-colors whitespace-nowrap"),
                        rx.link("For Retailers", href="#", class_name="text-gray-300 hover:text-white transition-colors whitespace-nowrap"),
                        rx.link("Support", href="#", class_name="text-gray-300 hover:text-white transition-colors whitespace-nowrap"),
                        class_name="flex gap-10 items-center"
                    ),
                    rx.spacer(),
                    rx.link("Sign In", href="#", class_name="text-gray-300 hover:text-white transition-colors whitespace-nowrap"),
                    rx.button(
                        "Schedule Demo",
                        class_name="bg-red-600 text-white px-4 py-2 rounded-full shadow hover:bg-red-700 transition text-sm font-semibold whitespace-nowrap"
                    ),
                    class_name="flex justify-center items-center py-6 px-8"
                ),
                class_name="flex justify-center"
            ),
rx.vstack(
    rx.vstack(
        rx.text(
            "Enforce your Amazon prices.",
            class_name="font-bold text-5xl text-center text-white max-w-3xl mx-auto mb-4"
        ),
        rx.text(
            "The only tool to actually enforce your MAP pricing.",
            class_name="text-gray-400 text-center max-w-xl mx-auto mb-8 text-lg"
        ),
        rx.button(
            "Schedule Demo →",
            class_name="bg-red-600 text-white px-6 py-3 rounded-full shadow hover:bg-red-700 transition text-sm font-semibold mx-auto whitespace-nowrap"
        ),
        class_name="space-y-4 px-4 text-center"
    ),
    rx.box(
        rx.image(
            src="imgtenis.png",
            alt="Tenis Listings",
            class_name="mx-auto rounded-2xl shadow-md w-[830px] h-auto"
        ),
        class_name="flex justify-center px-4 mt-10"
    ),
    class_name="space-y-12"
),
            rx.hstack(
                rx.box(
                    rx.vstack(
                        rx.text(
                            "And the current enforcement options",
                            class_name="text-white text-3xl font-semibold leading-tight"
                        ),
                        rx.text(
                            "suck even more.",
                            class_name="text-red-600 text-3xl font-semibold leading-tight mb-4"
                        ),
                        rx.text(
                            "Amazon brand protection and MAP enforcement have been issues on the platform since the beginning. The only current solution is to send out unhelpful compliance notifications which don’t address the underlying problem. The MAP pricing notifications only create more time-consuming work for your brand by asking you to rectify the MAP violation yourself.",
                            class_name="text-gray-400 text-sm max-w-md"
                        ),
                        class_name="space-y-2"
                    ),
                    class_name="flex-1 px-4"
                ),
                rx.image(
                    src="imgsec22.png",
                    alt="Competitor Notifications",
                    class_name="w-80 rounded-xl shadow-md"
                ),
                class_name="flex flex-col md:flex-row items-center justify-between gap-8 mb-16"
            ),
rx.vstack(
    rx.vstack(
        rx.hstack(
            rx.text(
                "So, we added ",
                class_name="text-white font-bold text-4xl"
            ),
            rx.text(
                "automatic MAP enforcement too.",
                class_name="text-red-600 font-bold text-4xl"
            ),
            class_name="flex flex-wrap text-left justify-start"
        ),
        rx.text(
            "MapAuthority makes it physically impossible for your third-party sellers to violate your MAP policy on Amazon. If a seller attempts to lower a product's price below your MAP policy, MapAuthority will automatically deny the request, and the violating price will never make it to the Amazon detail page. It is the ultimate Amazon MAP enforcement tool on the market today. Many of our users call it magic. We just call it proper MAP enforcement.",
            class_name="text-gray-400 text-left max-w-2xl text-sm mt-4"
        ),
        class_name="space-y-4 text-left"
    ),
rx.hstack(
    rx.image(
        src="img3.png",
        alt="Syncing Catalog",
        class_name="w-full max-w-xs rounded-xl shadow-md"
    ),
    rx.image(
        src="img33.png",
        alt="Product Enforcement",
        class_name="w-full max-w-xs rounded-xl shadow-md"
    ),
    class_name="flex justify-center gap-10 mt-8"
),
    class_name="space-y-8 mb-16 px-4"
),
            rx.box(
                rx.hstack(
                    rx.vstack(
                        rx.image(
                            src="logon.png",
                            alt="MapAuthority Logo",
                            class_name="h-30 w-auto"
                        ),
                        rx.text(
                            "MAP Authority’s patent pending software is the only tool on the market to truly enforce your MAP pricing on Amazon.",
                            class_name="text-gray-500 text-sm max-w-xs"
                        ),
                        rx.hstack(
                            rx.link(rx.icon("fa fa-facebook"), href="#", class_name="text-gray-500 hover:text-black transition-colors"),
                            rx.link(rx.icon("fa fa-instagram"), href="#", class_name="text-gray-500 hover:text-black transition-colors"),
                            rx.link(rx.icon("fa fa-linkedin"), href="#", class_name="text-gray-500 hover:text-black transition-colors"),
                            rx.link(rx.icon("fa fa-twitter"), href="#", class_name="text-gray-500 hover:text-black transition-colors"),
                            class_name="space-x-4 mt-4"
                        ),
                        class_name="flex-1 space-y-4"
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Contact", class_name="font-semibold text-black mb-2"),
                            rx.text("info@mapauthority.com", class_name="text-gray-500 text-sm"),
                            rx.text("Live Chat", class_name="text-gray-500 text-sm"),
                            rx.text("4210 Flagstaff Cove\nFort Wayne, IN 46815", class_name="text-gray-500 text-sm whitespace-pre-line"),
                            class_name="space-y-1"
                        ),
                        rx.vstack(
                            rx.text("Navigation", class_name="font-semibold text-black mb-2"),
                            rx.link("30-Day Free Trial", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            rx.link("Overview", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            rx.link("Blog", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            rx.link("For Retailers", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            rx.link("Support Hub", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            rx.link("Contact", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            rx.link("Sign In", href="#", class_name="text-gray-500 text-sm hover:text-black transition-colors"),
                            class_name="space-y-1"
                        ),
                        class_name="flex gap-16"
                    ),
                    rx.vstack(
                        rx.text("Subscribe to New Blog Posts", class_name="font-semibold text-black mb-2"),
                        rx.input(
                            placeholder="Enter your email address",
                            class_name="bg-gray-100 rounded px-4 py-2 text-sm"
                        ),
                        rx.button(
                            "Subscribe",
                            class_name="bg-red-600 text-white px-4 py-2 rounded-full shadow hover:bg-red-700 transition text-sm font-semibold mt-2"
                        ),
                        class_name="flex-1"
                    ),
                    class_name="flex flex-col md:flex-row justify-between items-start gap-8 py-10 border-t border-gray-200"
                ),
                rx.hstack(
                    rx.text("© 2025 MapAuthority | All Rights Reserved", class_name="text-xs text-gray-400"),
                    rx.spacer(),
                    rx.hstack(
                        rx.link("Privacy Policy", href="#", class_name="text-xs text-gray-400 hover:text-black transition-colors"),
                        rx.text("|", class_name="text-xs text-gray-400"),
                        rx.link("Terms of Service", href="#", class_name="text-xs text-gray-400 hover:text-black transition-colors"),
                        class_name="space-x-2"
                    ),
                    class_name="pt-4 border-t border-gray-200 mt-4"
                ),
                class_name="bg-white px-8"
            ),
            class_name="space-y-16 bg-black p-8 min-h-screen"
        ),
        class_name="bg-black"
    )

app = rx.App()
app.add_page(index)