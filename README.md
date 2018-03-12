# Bootstrap Sources

Twitter bootstrap sources as python package. Now you can add the bootstrap scss sources to your project without
using npm or copying files.

## Usage in Django apps

Use the great [django-sass-processor](https://github.com/jrief/django-sass-processor) and add this to `settings.py`:

``` python
import bootstrap_sources
# ...
SASS_PRECISION = 8  # required for bootstrap
SASS_PROCESSOR_INCLUDE_DIRS = [bootstrap_sources.scss_path(),]
```

With this, the [django-sass-processor](https://github.com/jrief/django-sass-processor) will find the bootstrap sources.
For example, extend bootstrap with your own `site.scss`:

``` scss
// Your variable overrides
$theme-colors: (
  primary: hotpink,
);

// Bootstrap and its default variables
@import "bootstrap";
```
