# Contributing

Please discuss changes to this project via email or issue before making it. We have a few guidelines in place to ensure that we can manage these changes and ensure the best possible code.

## Making Changes

* Fork the repository.
* Create a topic branch based on the `dev` branch.
 * You can create a topic branch with `git checkout -b myfeature dev`.
* Make commits in logical units.
* Check for unnecessary whitespace before committing.
* Make sure your commit message in the correct imperative format with a proper signoff.

```
[issues]Fix #5: Implement issue listing

```
 * It should begin with the area you are making changes to in brackets, followed by the issue the changes close (if applicable) and then a brief **descriptive** description. 
 * You can include the signoff with a `git commit -s`.
 * Signing off indicates you agree to the Developer Certificate of Origin (<http://developercertificate.org/>) with your legal name or your name claimed by legitimate use or repute.
 ```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

 ```
 * If you forget to signoff, you can include the line in a comment on your pull request.

## Submitting Changes
* Push you changes to a topic branch in your fork and ensure it is rebased with the latest `dev` branch.
* Submit a pull request to the repository.
* After review from 



## Branch/Release Policy
* All changes by PR should be based off the `dev` branch.
* Only the maintainer(s) should push to the `master` branch, which is the basis for all releases.
* Releases may be issued by creating a new tag in the form `v.1.2.3`.

## Attribution
These contributing guidelines are loosely based on the [guidelines](https://github.com/puppetlabs/puppet/blob/master/CONTRIBUTING.md) of Puppet.


