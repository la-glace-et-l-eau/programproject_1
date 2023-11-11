# Fetch libproj source code from Github

include(FetchContent)

FetchContent_Declare(
  libraryproject
  GIT_REPOSITORY https://github.com/la-glace-et-l-eau/libraryproject
  GIT_TAG        main
)

FetchContent_MakeAvailable(libraryproject)

message("Fetched libraryproject source code from Github: ${libraryproject_SOURCE_DIR}")
include_directories(
  ${libraryproject_SOURCE_DIR}
  ${libraryproject_BINARY_DIR}
)

